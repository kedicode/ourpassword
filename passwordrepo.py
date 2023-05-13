import csv


class PasswordRepo:

    def __init__(self, filename):

        assert filename != ''
        self.data = {}
        self.source_file = filename

    def load_data(self):
        with open(self.source_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data[f"{row['site']}_{row['username']}"] = (row['url'], row['password'])

    def get_all(self):
        return self.data

    def get_by_site(self, site_name):
        for key, value in self.data.items():
            (site, username) = key.split('_')
            if site == site_name or username == site_name:
                return site, username, self.data[key][0], self.data[key][1]

    def add_site(self, site, url, username, password):
        with open(self.source_file, newline='', mode='a') as f:
            password_writer = csv.writer(f)
            password_writer.writerow([site, url, username, password])
