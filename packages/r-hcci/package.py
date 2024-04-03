# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcci(RPackage):
	"""Interval Estimation of Linear Models with Heteroskedasticity

	Calculates the interval estimates for the parameters of linear models with heteroscedastic regression using bootstrap - (Wild Bootstrap) and double bootstrap-t (Wild Bootstrap). It is also possible to calculate confidence intervals using the percentile bootstrap and percentile bootstrap double. The package can calculate consistent estimates of the covariance matrix of the parameters of linear regression models with heteroscedasticity of unknown form. The package also provides a function to consistently calculate the covariance matrix of the parameters of linear models with heteroscedasticity of unknown form. The bootstrap methods exported by the package are based on the master's thesis of the first author, available at <https://raw.githubusercontent.com/prdm0/hcci/master/references/dissertacao_mestrado.pdf>. The hcci package in previous versions was cited in the book VINOD, Hrishikesh D. Hands-on Intermediate Econometrics Using R: Templates for Learning Quantitative Methods and R Software. 2022, p. 441, ISBN 978-981-125-617-2 (hardcover). The simple bootstrap schemes are based on the works of Cribari-Neto F and Lima M. G. (2009) <doi:10.1080/00949650801935327>, while the double bootstrap schemes for the parameters that index the linear models with heteroscedasticity of unknown form are based on the works of Beran (1987) <doi:10.2307/2336685>. The use of bootstrap for the calculation of interval estimates in regression models with heteroscedasticity of unknown form from a weighting of the residuals was proposed by Wu (1986) <doi:10.1214/aos/1176350142>. This bootstrap scheme is known as weighted or wild bootstrap.
	"""
	
	homepage = "https://github.com/prdm0/hcci"
	cran = "hcci" 

	version("1.1.0", md5="c5b19b77bc5bf59568da04bfce312a73")

