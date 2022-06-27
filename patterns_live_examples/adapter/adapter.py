class FromTxtToJsonAdapter:

    def __init__(self, file_path):
        self.file_path = file_path

    def convert_from_txt_to_json(self):
        with open(self.file_path) as file:
            lines = file.readlines()

        headers_txt = lines[0]
        user_data_txt = lines[1:]
        headers = headers_txt.split(',')
        data = [item.replace(r"\n", '').split(',') for item in user_data_txt]
        result = []
        for user_data in data:
            result.append(dict(zip(headers, user_data)))
        return result


print(FromTxtToJsonAdapter('users.txt').convert_from_txt_to_json())
