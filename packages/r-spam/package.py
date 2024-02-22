# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpam(RPackage):
	"""SPArse Matrix.

	Set of functions for sparse matrix algebra. Differences with other sparse
	matrix packages are: (1) we only support (essentially) one sparse matrix
	format, (2) based on transparent and simple structure(s), (3) tailored for
	MCMC calculations within G(M)RF. (4) and it is fast and scalable (with the
	extension package spam64). Documentation about 'spam' is provided by
	vignettes included in this package, see also Furrer and Sain (2010)
	<doi:10.18637/jss.v036.i10>; see 'citation("spam")' for details."""

	cran = "spam"

	version("2.10-0", md5="544bbc0a7ae76ef34ed01bf61c666f82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dotcall64", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
