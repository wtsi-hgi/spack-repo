# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogmult(RPackage):
	"""Log-Multiplicative Models, Including Association Models

	Functions to fit log-multiplicative models using 'gnm', with
  support for convenient printing, plots, and jackknife/bootstrap
  standard errors. For complex survey data, models can be fitted from
  design objects from the 'survey' package. Currently supported models
  include UNIDIFF (Erikson & Goldthorpe, 1992),
  a.k.a. log-multiplicative layer effect model (Xie, 1992)
  <doi:10.2307/2096242>, and several association models:
  Goodman (1979) <doi:10.2307/2286971>
  row-column association models of the RC(M) and RC(M)-L families
  with one or several dimensions; two skew-symmetric association
  models proposed by Yamaguchi (1990) <doi:10.2307/271086>
  and by van der Heijden & Mooijaart (1995) <doi:10.1177/0049124195024001002>
  Functions allow computing the intrinsic association coefficient
  (see Bouchet-Valat (2022) <doi:10.1177/0049124119852389>)
  and the Altham (1970) index <doi:10.1111/j.2517-6161.1970.tb00816.x>,
  including via the Bayes shrinkage estimator proposed
  by Zhou (2015) <doi:10.1177/0081175015570097>;
  and the RAS/IPF/Deming-Stephan algorithm.
	"""
	
	homepage = "https://github.com/nalimilan/logmult"
	cran = "logmult" 

	version("0.7.4", md5="aeb4fb29ef3a98fa287ee7a1dfb6431d")

	depends_on("r-gnm@1.0.5:", type=("build", "run"))
	depends_on("r-qvcalc", type=("build", "run"))
