# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRolwinmulcor(RPackage):
	"""Subroutines to Estimate Rolling Window Multiple Correlation

	Rolling Window Multiple Correlation ('RolWinMulCor') estimates the rolling (running) window correlation for the bi- and multi-variate cases between regular (sampled on identical time points) time series, with especial emphasis to ecological data although this can be applied to other kinds of data sets. 'RolWinMulCor' is based on the concept of rolling, running or sliding window and is useful to evaluate the evolution of correlation through time and time-scales. 'RolWinMulCor' contains six functions. The first two focus on the bi-variate case: (1) rolwincor_1win() and (2) rolwincor_heatmap(), which estimate the correlation coefficients and the their respective p-values for only one window-length (time-scale) and considering all possible window-lengths or a band of window-lengths, respectively. The second two functions: (3) rolwinmulcor_1win() and (4) rolwinmulcor_heatmap() are designed to analyze the multi-variate case, following the bi-variate case to visually display the results, but these two approaches are methodologically different. That is, the multi-variate case estimates the adjusted coefficients of determination instead of the correlation coefficients. The last two functions: (5) plot_1win() and (6) plot_heatmap() are used to represent graphically the outputs of the four aforementioned functions as simple plots or as heat maps. The functions contained in 'RolWinMulCor' are highly flexible since these contains several parameters to control the estimation of correlation and the features of the plot output, e.g. to remove the (linear) trend contained in the time series under analysis, to choose different p-value correction methods (which are used to address the multiple comparison problem) or to personalise the plot outputs. The 'RolWinMulCor' package also provides examples with synthetic and real-life ecological time series to exemplify its use. Methods derived from H. Abdi. (2007) <https://personal.utdallas.edu/~herve/Abdi-MCC2007-pretty.pdf>, R. Telford (2013) <https://quantpalaeo.wordpress.com/2013/01/04/, J. M. Polanco-Martinez (2019) <doi:10.1007/s11071-019-04974-y>, and J. M. Polanco-Martinez (2020) <doi:10.1016/j.ecoinf.2020.101163>. 
	"""
	
	cran = "RolWinMulCor" 

	version("1.2.0", md5="879ad4d91854a6f3f7eae56b25619131")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
