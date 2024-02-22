# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfedata(RPackage):
	"""Example SpatialFeatureExperiment datasets

	Example spatial transcriptomics datasets with Simple Feature annotations as SpatialFeatureExperiment objects. Technologies include Visium, slide-seq, Nanostring CoxMX, Vizgen MERFISH, and 10X Xenium. Tissues include mouse skeletal muscle, human melanoma metastasis, human lung, breast cancer, and mouse liver.
	"""
	
	homepage = "https://github.com/pachterlab/SFEData"
	bioc = "SFEData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SFEData_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SFEData/SFEData_1.4.0.tar.gz"]

	version("1.4.0", md5="7f3376870c972cba309b26d52d24fcbb")

	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment