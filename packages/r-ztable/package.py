# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZtable(RPackage):
    """Zebra-Striped Tables in LaTeX and HTML Formats
    
    Makes zebra-striped tables (tables with alternating row colors)
    in LaTeX and HTML formats easily from a data.frame, matrix, lm, aov, anova,
    glm, coxph, nls, fitdistr, mytable and cbind.mytable objects.
    """

    homepage = "https://cran.r-project.org/web/packages/ztable"
    
    cran = "ztable"

    # versions
    version("0.2.3", md5="b9f462e4cc1f571d6dc5f621f93ca31a")
    

    # dependencies
    depends_on("r@3.1.2:", type=('build', 'run'))
    depends_on("r-stringr", type=('build', 'run'))
    depends_on("r-magrittr", type=('build', 'run'))
    depends_on("r-color-brewer", type=('build', 'run'))
    depends_on("r-flextable", type=('build', 'run'))
    depends_on("r-officer", type=('build', 'run'))
    depends_on("r-rstudioapi", type=('build', 'run'))
    depends_on("r-scales", type=('build', 'run'))
    
