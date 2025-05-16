# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class REasyqc2(RPackage):
    """EasyQC2 is an extension of the previous EasyQC R-package that provides advanced and improved functionality. """

    homepage = "https://www.example.com"
    url = "https://homepages.uni-regensburg.de/~wit59712/easyqc2/EasyQC2_1.1.2.tar.gz"

    version("1.1.2", sha256="088e8ca3418bb75233235380426f64ded034474f103e4d3e30ecd859306691ff", url="https://homepages.uni-regensburg.de/~wit59712/easyqc2/EasyQC2_1.1.2.tar.gz")

    depends_on("r-cairo", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-forestplot", type=("build", "run"))
