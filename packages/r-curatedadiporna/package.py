# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadiporna(RPackage):
	"""A Curated RNA-Seq Dataset of MDI-induced Differentiated Adipocytes (3T3-L1)

	A curated dataset of RNA-Seq samples. The samples are MDI-induced pre-phagocytes (3T3-L1) at different time points/stage of differentiation. The package document the data collection, pre-processing and processing. In addition to the documentation, the package contains the scripts that was used to generated the data.
	"""
	
	homepage = "https://github.com/MahShaaban/curatedAdipoRNA"
	bioc = "curatedAdipoRNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedAdipoRNA_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedAdipoRNA/curatedAdipoRNA_1.18.0.tar.gz"]

	version("1.18.0", sha256="3791a38e8c648d504be4a0eafd893b1b822012add17833c04d68b2c0ef45c5b7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

