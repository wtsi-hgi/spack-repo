# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaaslin2(RPackage):
    """ "Multivariable Association Discovery in Population-scale Meta-omics Studies"

    MaAsLin2 is comprehensive R package for efficiently determining multivariable association between clinical metadata and microbial meta'omic features. MaAsLin2 relies on general linear models to accommodate most modern epidemiological study designs, including cross-sectional and longitudinal, and offers a variety of data exploration, normalization, and transformation methods. MaAsLin2 is the next generation of MaAsLin.
    """

    homepage = "http://huttenhower.sph.harvard.edu/maaslin2"
    bioc = "Maaslin2"

    version("1.22.0", commit="fcec85e6f166949ed20d57875113c6404293c02f")
    version("1.16.0", commit="0ab531d6648aef776042bd155f6f52b22fedb9fc")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-robustbase", type=("build", "run"))
    depends_on("r-biglm", type=("build", "run"))
    depends_on("r-pcapp", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-metagenomeseq", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-chemometrics", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-logging", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-lmertest", type=("build", "run"))
    depends_on("r-hash", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-glmmtmb", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-cplm", type=("build", "run"))
    depends_on("r-pscl", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
