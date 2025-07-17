# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcy3(RPackage):
    """Functions to Access and Control Cytoscape

    Vizualize, analyze and explore networks using Cytoscape via R. Anything you can do using the graphical user interface of Cytoscape, you can now do with a single RCy3 function.
    """

    homepage = "https://github.com/cytoscape/RCy3"
    bioc = "RCy3"

    version("2.28.1", commit="2dbd87af8f020732d92f8619036e823c34ce64ae")
    version("2.22.1", commit="cd4cb1bf320f0dac9f13264a01dbd6cf75a6eec4")

    depends_on("r-httr", type=("build", "run"))
    depends_on("r-rjsonio", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-uuid", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-base64url", type=("build", "run"))
    depends_on("r-base64enc", type=("build", "run"))
    depends_on("r-irkernel", type=("build", "run"))
    depends_on("r-irdisplay", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
