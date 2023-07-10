# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpubr(RPackage):
    """Generate Publication Ready Visualizations of Single Cell
Transcriptomics Data
    
    A system that provides a streamlined way of generating publication ready plots for known Single-Cell transcriptomics data in a “publication ready” format. This is, the goal is to automatically generate plots with the highest quality possible, that can be used right away or with minimal modifications for a research article.
    """

    homepage = "https://cran.r-project.org/web/packages/SCpubr"
    
    cran = "SCpubr"

    # versions
    version("1.1.2", md5="21738379760ec2b1811187131f02adbd")
    

    # dependencies
    depends_on("r@4.0.0:", type=('build', 'run'))
    
