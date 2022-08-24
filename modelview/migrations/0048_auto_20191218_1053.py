# Generated by Django 3.0 on 2019-12-18 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelview", "0047_auto_20191021_1525"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basicfactsheet",
            name="license",
            field=models.CharField(
                choices=[
                    ("Academic Free License v3.0", "Academic Free License v3.0"),
                    ("Apache license 2.0", "Apache license 2.0"),
                    ("Artistic license 2.0", "Artistic license 2.0"),
                    ("Boost Software License 1.0", "Boost Software License 1.0"),
                    (
                        'BSD 2-clause "Simplified" license',
                        'BSD 2-clause "Simplified" license',
                    ),
                    ("BSD 3-clause Clear license", "BSD 3-clause Clear license"),
                    (
                        "Creative Commons license family",
                        "Creative Commons license family",
                    ),
                    (
                        "Creative Commons Zero v1.0 Universal",
                        "Creative Commons Zero v1.0 Universal",
                    ),
                    (
                        "Creative Commons Attribution 4.0",
                        "Creative Commons Attribution 4.0",
                    ),
                    (
                        "Creative Commons Attribution Share Alike 4.0",
                        "Creative Commons Attribution Share Alike 4.0",
                    ),
                    (
                        "Do What The F*ck You Want To Public License",
                        "Do What The F*ck You Want To Public License",
                    ),
                    (
                        "Educational Community License v2.0",
                        "Educational Community License v2.0",
                    ),
                    ("Eclipse Public License 1.0", "Eclipse Public License 1.0"),
                    (
                        "European Union Public License 1.1",
                        "European Union Public License 1.1",
                    ),
                    (
                        "GNU Affero General Public License v3.0",
                        "GNU Affero General Public License v3.0",
                    ),
                    (
                        "GNU General Public License family",
                        "GNU General Public License family",
                    ),
                    (
                        "GNU General Public License v2.0",
                        "GNU General Public License v2.0",
                    ),
                    (
                        "GNU General Public License v3.0",
                        "GNU General Public License v3.0",
                    ),
                    (
                        "GNU Lesser General Public License family",
                        "GNU Lesser General Public License family",
                    ),
                    (
                        "GNU Lesser General Public License v2.1",
                        "GNU Lesser General Public License v2.1",
                    ),
                    (
                        "GNU Lesser General Public License v3.0",
                        "GNU Lesser General Public License v3.0",
                    ),
                    ("ISC", "ISC"),
                    (
                        "LaTeX Project Public License v1.3c",
                        "LaTeX Project Public License v1.3c",
                    ),
                    ("Microsoft Public License", "Microsoft Public License"),
                    ("MIT", "MIT"),
                    ("Mozilla Public License 2.0", "Mozilla Public License 2.0"),
                    ("Open Software License 3.0", "Open Software License 3.0"),
                    ("PostgreSQL License", "PostgreSQL License"),
                    ("SIL Open Font License 1.1", "SIL Open Font License 1.1"),
                    (
                        "University of Illinois/NCSA Open Source License",
                        "University of Illinois/NCSA Open Source License",
                    ),
                    ("The Unlicense", "The Unlicense"),
                    ("zLib License", "zLib License"),
                    (
                        "BSD 3-clause 'New' or 'Revised' license",
                        "BSD 3-clause 'New' or 'Revised' license",
                    ),
                    ("Other", "Other"),
                    ("Unknown", "Unknown"),
                ],
                default="Unknown",
                max_length=50,
                verbose_name="License",
            ),
        ),
    ]
