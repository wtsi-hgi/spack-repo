# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsn(RPackage):
	"""Variance stabilization and calibration for microarray data.

	The package implements a method for normalising microarray intensities,
	and works for single- and multiple-color arrays. It can also be used for
	data from other technologies, as long as they have similar format. The
	method uses a robust variant of the maximum-likelihood estimator for an
	additive-multiplicative error model and affine calibration. The model
	incorporates data calibration step (a.k.a. normalization), a model for
	the dependence of the variance on the mean intensity and a variance
	stabilizing data transformation. Differences between transformed
	intensities are analogous to "normalized log-ratios". However, in
	contrast to the latter, their variance is independent of the mean, and
	they are usually more sensitive and specific in detecting differential
	transcription."""

	bioc = "vsn"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/vsn_3.70.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/vsn/vsn_3.70.0.tar.gz"]

	version("3.70.0", md5="1c9484f361b22f76135af5567306f0c6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
