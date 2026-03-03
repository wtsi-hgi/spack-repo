# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmar(RPackage):
	"""Empirical Model Assessment

	A tool that allows users to generate various indices for evaluating statistical models. The fitstat() function computes indices based on the fitting data. The valstat() function computes indices based on the validation data set. Both fitstat() and valstat() will return 16 indices SSR: residual sum of squares, TRE: total relative error, Bias: mean bias, MRB: mean relative bias, MAB: mean absolute bias, MAPE: mean absolute percentage error, MSE: mean squared	error, RMSE: root mean square error, Percent.RMSE: percentage root mean squared error, R2: coefficient of determination, R2adj: adjusted coefficient of determination, APC: Amemiya's prediction criterion, logL: Log-likelihood, AIC: Akaike information criterion, AICc: corrected Akaike information criterion, BIC: Bayesian information criterion, HQC: Hannan-Quin information criterion. The	lower the better for the SSR, TRE, Bias, MRB, MAB, MAPE, MSE, RMSE, Percent.RMSE, APC, AIC, AICc, BIC and HQC indices. The higher the better for R2 and R2adj indices. Petre Stoica, P., Selén, Y. (2004) <doi:10.1109/MSP.2004.1311138>n Zhou et al. (2023) <doi:10.3389/fpls.2023.1186250>n Ogana, F.N., Ercanli, I. (2021) <doi:10.1007/s11676-021-01373-1>n Musabbikhah et al. (2019) <doi:10.1088/1742-6596/1175/1/012270>.
	"""
	
	cran = "EMAR" 

	version("1.0.0", md5="54d25f551506bb5a0f3a203f9e3060e7")

