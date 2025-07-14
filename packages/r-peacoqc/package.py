# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeacoqc(RPackage):
	"""Peak-based selection of high quality cytometry data

	This is a package that includes pre-processing and quality control functions that can remove margin events, compensate and transform the data and that will use PeacoQCSignalStability for quality control. This last function will first detect peaks in each channel of the flowframe. It will remove anomalies based on the IsolationTree function and the MAD outlier detection method. This package can be used for both flow- and mass cytometry data.
	"""
	
	homepage = "http://github.com/saeyslab/PeacoQC"
	bioc = "PeacoQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PeacoQC_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PeacoQC/PeacoQC_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="1c9b1792e532b816d4859bc4769b3e5fdaae3632ed837d7bb9c25f4f53b40884")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowworkspace", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
