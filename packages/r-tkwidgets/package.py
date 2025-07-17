# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkwidgets(RPackage):
    """R based tk widgets

    Widgets to provide user interfaces. tcltk should have been installed for the widgets to run.
    """

    bioc = "tkWidgets"

    version("1.86.0", commit="eb5e53b6faaf3b85b79cc0e42fe0917887547677")
    version("1.80.0", commit="7b630839f778bdf5ddf9313edf2035ff0c833c87")

    depends_on("r@2:", type=("build", "run"))
    depends_on("r-widgettools@1.1.7:", type=("build", "run"))
    depends_on("r-dyndoc@1.3:", type=("build", "run"))
