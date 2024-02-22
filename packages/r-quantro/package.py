# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantro(RPackage):
	"""A test for when to use quantile normalization.

	A data-driven test for the assumptions of quantile normalization using
	raw data such as objects that inherit eSets (e.g. ExpressionSet,
	MethylSet). Group level information about each sample (such as Tumor /
	Normal status) must also be provided because the test assesses if there
	are global differences in the distributions between the user-defined
	groups."""

	bioc = "quantro"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/quantro_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/quantro/quantro_1.36.0.tar.gz"]

	version("1.36.0", md5="3e7912df8d9bc50c461074539540f289")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
