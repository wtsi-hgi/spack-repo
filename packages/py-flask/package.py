# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlask(PythonPackage):
    """A simple framework for building complex web applications."""

    homepage = "https://flask.palletsprojects.com/"
    pypi = "Flask/Flask-3.1.2.tar.gz"

    license("BSD-3-Clause")

    version("3.1.2", sha256="bf656c15c80190ed628ad08cdfd3aaa35beb087855e2f494910aa3774cc4fd87")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-flit-core@3.12:", type="build")

    depends_on("py-blinker@1.9.0:", type=("build", "run"))
    depends_on("py-click@8.1.3:", type=("build", "run"))
    depends_on("py-itsdangerous@2.2.0:", type=("build", "run"))
    depends_on("py-jinja2@3.1.2:", type=("build", "run"))
    depends_on("py-markupsafe@2.1.1:", type=("build", "run"))
    depends_on("py-werkzeug@3.1.0:", type=("build", "run"))
    depends_on("py-importlib-metadata@3.6.0:", type=("build", "run"), when="^python@:3.9")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            flask = Executable(join_path(self.prefix.bin, "flask"))
            flask("--help")
