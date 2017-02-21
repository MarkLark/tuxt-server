#!/usr/bin/python

if __name__ == '__main__':
    from app import create_app, models
    app, api = create_app( config = "configs.local", models = models.models )

    with app.app_context():
        print "Creating All Storage"
        api.store.create_all()
        models.os.add_defaults( api.store )
        models.app.add_defaults( api.store )

        print "OS.Distro"
        models.os.Distro.print_table()

        print "OS.OS"
        models.os.OS.print_table()

        print "OS.Version"
        models.os.Version.print_table()


        print "App"
        models.app.App.print_table()

        print "App.Version"
        models.app.Version.print_table()

        print "App.Category"
        models.app.Category.print_table()

        print "App.SubCategory"
        models.app.SubCategory.print_table()

        #
    app.run( host = "0.0.0.0", port = 5000, debug = True, use_reloader = False )

    with app.app_context():
        api.store.destroy_all()
