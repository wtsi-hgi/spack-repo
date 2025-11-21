# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RUcscUtils(RPackage):
    """ A set of low-level utilities to retrieve data from the UCSC Genome Browser. Most functions in the package access the data via the UCSC REST API but some of them query the UCSC MySQL server directly. Note that the primary purpose of the package is to support higher-level functionalities implemented in downstream packages like GenomeInfoDb or txdbmaker. """

    homepage = "https://bioconductor.org/packages/release/bioc/html/UCSC.utils.html"
    url = "https://bioconductor.org/packages/3.22/bioc/src/contrib/UCSC.utils_1.6.0.tar.gz"
    bioc = "UCSC.utils"

    version("1.6.0", sha256="3ec811f3bddb736f762db888cc26dcf98b0d21659a939580490551bd46238b7a")
    version("1.4.0", sha256="db2680cf8a94a2119783905487b5a9711006c295641f415cf4e79235c83d1a26", url="https://bioconductor.org/packages/3.21/bioc/src/contrib/UCSC.utils_1.4.0.tar.gz")

    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-s4vectors@:0.47.5", type=("build", "run"), when="@:1.5")
    depends_on("r-s4vectors@0.47.6:", type=("build", "run"), when="@1.6.0:")
