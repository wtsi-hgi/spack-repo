# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaics(RPackage):
    """MOSAiCS (MOdel-based one and two Sample Analysis and Inference for ChIP-Seq)

    This package provides functions for fitting MOSAiCS and MOSAiCS-HMM, a statistical framework to analyze one-sample or two-sample ChIP-seq data of transcription factor binding and histone modification.
    """

    homepage = "http://groups.google.com/group/mosaics_user_group"
    bioc = "mosaics"

    version("2.46.0", commit="536558b9ea33ec274213a3715110316ace0a9ac1")
    version("2.40.0", commit="b660aa1b0bd99645166ff38313615835ca8db03f")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("perl", type=("build", "link", "run"))
