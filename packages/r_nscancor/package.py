# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNscancor(RPackage):
	"""Non-Negative and Sparse CCA

	Two implementations of canonical correlation analysis
        (CCA) that are based on iterated regression. By choosing the
        appropriate regression algorithm for each data domain, it is
        possible to enforce sparsity, non-negativity or other kinds of
        constraints on the projection vectors. Multiple canonical
        variables are computed sequentially using a generalized
        deflation scheme, where the additional correlation not
        explained by previous variables is maximized. nscancor() is
        used to analyze paired data from two domains, and has the same
        interface as cancor() from the 'stats' package (plus some extra
        parameters). mcancor() is appropriate for analyzing data from
        three or more domains. See
        <https://sigg-iten.ch/learningbits/2014/01/20/canonical-correlation-analysis-under-constraints/>
        and Sigg et al. (2007) <doi:10.1109/MLSP.2007.4414315> for more
        details.
	"""
	
	homepage = "https://sigg-iten.ch/research/"
	cran = "nscancor" 

	version("0.7.0-6", md5="4d4405e2d653204405b3b906fec29de2")

	depends_on("r@3.6:", type=("build", "run"))
