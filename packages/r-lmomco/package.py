# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmomco(RPackage):
	"""L-Moments, Censored L-Moments, Trimmed L-Moments, L-Comoments,
and Many Distributions

	Extensive functions for Lmoments (LMs) and probability-weighted moments (PWMs),
  distribution parameter estimation, LMs for distributions, LM ratio diagrams, multivariate
  Lcomoments, and asymmetric (asy) trimmed LMs (TLMs). Maximum likelihood and
  maximum product spacings estimation are available. Right-tail and left-tail LM censoring
  by threshold or indicator variable are available. LMs of residual (resid) and reversed
  (rev) residual life are implemented along with 13 quantile operators for reliability analyses.
  Exact analytical bootstrap estimates of order statistics, LMs, and LM var-covars are available.
  Harri-Coble Tau34-squared Normality Test is available. Distributions with L, TL, and added
  (+) support for right-tail censoring (RC) encompass: Asy Exponential (Exp) Power [L],
  Asy Triangular [L], Cauchy [TL], Eta-Mu [L], Exp. [L], Gamma [L], Generalized (Gen) Exp
  Poisson [L], Gen Extreme Value [L], Gen Lambda [L, TL], Gen Logistic [L], Gen Normal [L],
  Gen Pareto [L+RC, TL], Govindarajulu [L], Gumbel [L], Kappa [L], Kappa-Mu [L],
  Kumaraswamy [L], Laplace [L], Linear Mean Residual Quantile Function [L], Normal [L],
  3p log-Normal [L], Pearson Type III [L], Polynomial Density-Quantile 3 and 4 [L],
  Rayleigh [L], Rev-Gumbel [L+RC], Rice [L], Singh Maddala [L], Slash [TL], 3p Student t [L],
  Truncated Exponential [L], Wakeby [L], and Weibull [L].
	"""
	
	homepage = "https://www.amazon.com/dp/1463508417/"
	cran = "lmomco" 

	version("2.4.14", md5="c47f124168f007802995d12ab284d4e7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-lmoments", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
