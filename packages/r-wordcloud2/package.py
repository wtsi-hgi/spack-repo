# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RWordcloud2(RPackage):
    """A fast visualization tool for creating wordcloud by using 'wordcloud2.js'."""

    homepage = "https://github.com/lchiffon/wordcloud2"
    cran = "wordcloud2"

    version("0.2.1", sha256="d3f4f49114a503ef206e64771b5160069b5095d7be6f807b8b041763972058a8")

    version("0.2.0", sha256="de1233499725be45ec8b7ea87e12793e34fb6bd40cb90d77d0c1549f65ac9a7a")
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-base64enc", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-webshot", type=("build", "run"))
