def format_list(list_, pattern):
    return [ pattern.format(str(s)) for s in list_]
    #return [pattern % s for s in list_]


class FilterModule(object):
    def filters(self):
        return {
                'format_list': format_list,
                }
