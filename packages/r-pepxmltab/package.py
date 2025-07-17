# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepxmltab(RPackage):
    """Parsing pepXML files and filter based on peptide FDR.

    Parsing pepXML files based one XML package. The package tries to handle pepXML files generated from different softwares. The output will be a peptide-spectrum-matching tabular file. The package also provide function to filter the PSMs based on FDR.
    """

    bioc = "pepXMLTab"

    version("1.42.0", commit="3712347bb7cf9b6f3e46bd4bfbaaa1fd8e5659d3")
    version("1.36.0", commit="fc6d53bb6d626ab96032b222b1ebe2b3d14bcf5d")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-xml@3.98.1.1:", type=("build", "run"))
