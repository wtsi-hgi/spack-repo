# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmidas(RPackage):
	"""Multiple Imputation with Denoising Autoencoders

	A tool for multiply imputing missing data using 'MIDAS', a deep learning method based on denoising autoencoder neural networks (see Lall and Robinson, 2022; <doi:10.1017/pan.2020.49>). This algorithm offers significant accuracy and efficiency advantages over other multiple imputation strategies, particularly when applied to large datasets with complex features. Alongside interfacing with 'Python' to run the core algorithm, this package contains functions for processing data before and after model training, running imputation model diagnostics, generating multiple completed datasets, and estimating regression models on these datasets. For more information see Lall and Robinson (2023) <doi:10.18637/jss.v107.i09>.
	"""
	
	homepage = "https://github.com/MIDASverse/rMIDAS"
	cran = "rMIDAS" 

	version("1.0.0", md5="89832cc8ffd161acee8db899dd404bd0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
