# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprscoredata(RPackage):
	"""Pre-trained models for the crisprScore package

	Provides an interface to access pre-trained models for on-target and off-target gRNA activity prediction algorithms implemented in the crisprScore package. Pre-trained model data are stored in the ExperimentHub database. Users should consider using the crisprScore package directly to use and load the pre-trained models.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprScoreData/issues"
	bioc = "crisprScoreData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/crisprScoreData_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/crisprScoreData/crisprScoreData_1.6.0.tar.gz"]

	version("1.6.0", md5="1f4d86404f045ec36cf7d1b1c64373fe")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

	# experiment