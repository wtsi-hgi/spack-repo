# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHornpa(RPackage):
	"""Horn's (1965) Test to Determine the Number of Components/Factors

	A stand-alone function that generates a user specified number of random datasets and computes eigenvalues using the random datasets (i.e., implements Horn's [1965, Psychometrika] parallel analysis <https://link.springer.com/article/10.1007/BF02289447>). Users then compare the resulting eigenvalues (the mean or the specified percentile) from the random datasets (i.e., eigenvalues resulting from noise) to the eigenvalues generated with the user's data. Can be used for both principal components analysis (PCA) and common/exploratory factor analysis (EFA). The output table shows how large eigenvalues can be as a result of merely using randomly generated datasets. If the user's own dataset has  actual eigenvalues greater than the corresponding eigenvalues, that lends support to retain that factor/component. In other words, if the i(th) eigenvalue from the actual data was larger than the percentile of the (i)th eigenvalue generated using randomly generated data, empirical support is provided to retain that factor/component. Horn, J. (1965). A rationale and test for the number of factors in factor analysis. Psychometrika, 32, 179-185.
	"""
	
	cran = "hornpa" 

	version("1.1.0", md5="b553c4a2800995606fbc4b13ef2910ba")

