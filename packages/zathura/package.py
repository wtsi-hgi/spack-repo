# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Zathura(MesonPackage):
    """Zathura is a highly customizable and functional document viewer
    based on the girara user interface library and several document libraries."""

    homepage = "https://pwmt.org/projects/zathura"
    url = "https://github.com/pwmt/zathura/archive/refs/tags/0.5.11.tar.gz"
    git = "https://github.com/pwmt/zathura.git"

    version("0.5.11", sha256="32540747a6fe3c4189ec9d5de46a455862c88e11e969adb5bc0ce8f9b25b52d4")

    # Required dependencies
    depends_on("gtkplus@3.24:", type=("build", "run", "link"))
    depends_on("glib@2.72:", type=("build", "run", "link"))
    depends_on("girara@0.4.3:", type=("build", "run", "link"))
    depends_on("json-glib", type=("build", "run", "link"))
    depends_on("sqlite@3.6.23:", type=("build", "run", "link"))
    depends_on("file", type=("build", "run", "link"))

    # Build dependencies
    depends_on("gettext", type="build")
