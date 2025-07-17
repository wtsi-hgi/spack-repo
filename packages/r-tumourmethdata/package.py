# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTumourmethdata(RPackage):
    """A Collection of DNA Methylation Datasets for Human Tumour Samples and Matching Normal Samples

    TumourMethData collects tumour methylation data from a variety of different tumour types (and also matching normal samples where available) and produced with different technologies (e.g. WGBS, RRBS and methylation arrays) and provides them as RangedSummarizedExperiments. This facilitates easy extraction of methylation data for regions of interest across different tumour types and studies.
    """

    homepage = "https://github.com/richardheery/TumourMethData"
    bioc = "TumourMethData"

    version("1.6.0", commit="fe4e42def3fb594bdfd6e4142df765b571a809bf")
    version("1.0.0", commit="3b8cb73f5af7d850eb2c97549a8100587a3359a3")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
