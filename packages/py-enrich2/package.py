# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyEnrich2(PythonPackage):
    """Enrich2 is a general software tool for processing, analyzing, and visualizing data from deep mutational scanning experiments."""

    homepage = "https://github.com/FowlerLab/Enrich2"
    git = "https://github.com/FowlerLab/Enrich2"

    version("1.3.1", tag="v1.3.1")

    depends_on("python@2.7.18+tkinter", type=("build", "run"))

    depends_on("py-numpy@1.10.4:1.15.0", type=("build", "run"))
    depends_on("py-scipy@0.16.0:1.2.1", type=("build", "run"))
    depends_on("py-pandas@0.18.0:0.25.0", type=("build", "run"))
    depends_on("py-tables@3.2.0:3.6.1", type=("build", "run"))
    depends_on("py-statsmodels@0.6.1:0.10.1", type=("build", "run"))
    depends_on("py-matplotlib@1.4.3:2.0.2", type=("build", "run"))
    depends_on("py-cython@:0.29.36", type=("build", "run"))
    depends_on("freetype", type=("build", "run"))
    depends_on("gcc", type=("build", "run"))

    def patch(self):
        filter_file("'console_scripts': ['enrich_cmd = enrich2.main:main_cmd'],", "", "setup.py", string=True)
        filter_file("'gui_scripts': ['enrich_gui = enrich2.main:main_gui'],", "", "setup.py", string=True)

    @run_after("install")
    def bin_install(self):
        mkdir(self.prefix.bin)
        with open(self.prefix.bin.enrich_cmd, "w") as f:
            f.write("#!/bin/bash\necho -e \"from enrich2.main import main_cmd\\nimport sys\\nsys.exit(main_cmd())\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + ":$LD_LIBRARY_PATH" + "\" python - \"$@\"")

        with open(prefix.bin.enrich_gui, "w") as f:
            f.write("#!/bin/bash\necho -e \"from enrich2.main import main_gui\\nimport sys\\nsys.exit(main_gui())\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + ":$LD_LIBRARY_PATH" + "\" python - \"$@\"")

        os.chmod(self.prefix.bin.enrich_cmd, 0o755)
        os.chmod(self.prefix.bin.enrich_gui, 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)

