# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyseurat(RPackage):
    """Brings Seurat to the Tidyverse
    
    It creates an invisible layer that allow to see the 'Seurat' object 
    as tibble and interact seamlessly with the tidyverse.
    """

    homepage = "https://cran.r-project.org/web/packages/tidyseurat"
    
    cran = "tidyseurat"

    # versions
    version("0.6.1", md5="01b183086ad91a4938db7f61e7522fd2")
    

    # dependencies
    depends_on("r-seurat", type=('build', 'run'))
    depends_on("r-tibble", type=('build', 'run'))
    depends_on("r-dplyr", type=('build', 'run'))
    depends_on("r-magrittr", type=('build', 'run'))
    depends_on("r-tidyr@1.2.0:", type=('build', 'run'))
    depends_on("r-ggplot2", type=('build', 'run'))
    depends_on("r-rlang", type=('build', 'run'))
    depends_on("r-purrr", type=('build', 'run'))
    depends_on("r-lifecycle", type=('build', 'run'))
    depends_on("r-plotly", type=('build', 'run'))
    depends_on("r-tidyselect", type=('build', 'run'))
    depends_on("r-ellipsis", type=('build', 'run'))
    depends_on("r-vctrs", type=('build', 'run'))
    depends_on("r-pillar", type=('build', 'run'))
    depends_on("r-stringr", type=('build', 'run'))
    depends_on("r-cli", type=('build', 'run'))
    depends_on("r-fansi", type=('build', 'run'))
    depends_on("r-matrix", type=('build', 'run'))
    
