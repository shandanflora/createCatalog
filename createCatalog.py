import xlrd
import xlwt
import Count


def read_excel(file):
    book = xlrd.open_workbook(file)
    dict_count = {}
    for sheet in book.sheets():
        count = Count.CountCase()
        count.finish_pass = sheet.col_values(sheet.ncols - 1, 1).count('PASS')
        count.finish_fail = sheet.col_values(sheet.ncols - 1, 1).count('FAIL')
        count.unfinished = sheet.col_values(sheet.ncols - 1, 1).count('')
        count.total = count.finish_fail + count.finish_pass + count.unfinished
        if sheet.name.find('对照表') == -1:
            item = {sheet.name: count}
            dict_count.update(item)
    return dict_count


def format_cell(style, font):
    # 设置单元格对齐方式
    alignment = xlwt.Alignment()
    alignment.horz = alignment.HORZ_CENTER
    alignment.vert = alignment.VERT_CENTER
    alignment.wrap = 1
    style.font = font  # 设定样式
    style.alignment = alignment


def draw_border(style):
    # draw border
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.bottom_colour = 0x3A
    style.borders = borders


def col_width(sheet, row_count):
    for i in range(row_count + 4):
        sheet.row(i).height_mismatch = True
        sheet.row(i).height = 256 * 2
    sheet.col(0).width = 256 * 29
    sheet.col(1).width = 256 * 14
    sheet.col(2).width = 256 * 8
    sheet.col(3).width = 256 * 8
    sheet.col(4).width = 256 * 10
    sheet.col(5).width = 256 * 8
    sheet.col(6).width = 256 * 8
    sheet.col(7).width = 256 * 35


def write_head(sheet, style, font):
    # heading
    sheet.write_merge(0, 0, 0, 7, '执行用例统计报告', style)
    # header
    font.height = 13 * 20
    font.bold = 1
    style.font = font  # 设定样式
    sheet.write_merge(1, 2, 0, 0, '测试模块', style)
    sheet.write_merge(1, 2, 1, 1, '测试项目数', style)
    sheet.write_merge(1, 1, 2, 3, '已完成（条）', style)
    sheet.write(2, 2, 'Pass', style)
    sheet.write(2, 3, 'Fail', style)
    sheet.write_merge(1, 2, 4, 4, '未完成（条）', style)
    sheet.write_merge(1, 1, 5, 6, '工时', style)
    sheet.write(2, 5, '小时', style)
    sheet.write(2, 6, '天', style)
    sheet.write_merge(1, 2, 7, 7, '说明', style)


def write_data(sheet_names, dict_result, style, sheet, row_count):
    total_total = 0
    total_finish_pass = 0
    total_finish_fail = 0
    total_unfinished = 0
    total_hour = 0
    total_day = 0
    for i in range(3, row_count + 3):
        sheet.write(i, 0, sheet_names[i - 3], style)
        total = dict_result[sheet_names[i - 3]].total
        finish_pass = dict_result[sheet_names[i - 3]].finish_pass
        finish_fail = dict_result[sheet_names[i - 3]].finish_fail
        unfinished = dict_result[sheet_names[i - 3]].unfinished
        hour = (dict_result[sheet_names[i - 3]].total / 60) * 8
        day = hour / 8
        sheet.write(i, 1, total, style)
        sheet.write(i, 2, finish_pass, style)
        sheet.write(i, 3, finish_fail, style)
        sheet.write(i, 4, unfinished, style)
        sheet.write(i, 5, hour, style)
        sheet.write(i, 6, day, style)
        sheet.write(i, 7, '', style)
        total_total += total
        total_finish_pass += finish_pass
        total_finish_fail += finish_fail
        total_unfinished += unfinished
        total_hour += hour
        total_day += day
    sheet.write(row_count + 3, 0, '总计', style)
    sheet.write(row_count + 3, 1, total_total, style)
    sheet.write(row_count + 3, 2, total_finish_pass, style)
    sheet.write(row_count + 3, 3, total_finish_fail, style)
    sheet.write(row_count + 3, 4, total_unfinished, style)
    sheet.write(row_count + 3, 5, total_hour, style)
    sheet.write(row_count + 3, 6, total_day, style)


def write_excel(file, dict_result):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Count')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = '微软雅黑'
    font.height = 15*20
    format_cell(style, font)
    draw_border(style)
    sheet_names = list(dict_result.keys())
    row_count = len(sheet_names)
    col_width(sheet, row_count)
    write_head(sheet, style, font)
    # data
    font.height = 12 * 20
    font.bold = 0
    style.font = font  # 设定样式

    write_data(sheet_names, dict_result, style, sheet, row_count)

    sheet.set_panes_frozen(True)
    sheet.set_horz_split_pos(1)
    sheet.set_horz_split_pos(2)
    sheet.set_horz_split_pos(3)
    book.save(file)
    print('write excel successfully!!!')


if __name__ == '__main__':
    write_excel('123.xlsx', read_excel('/Users/user-b016/Desktop/111/拖地机器人测试用例.xlsx'))