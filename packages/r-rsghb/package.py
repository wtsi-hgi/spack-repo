# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsghb(RPackage):
	"""Functions for Hierarchical Bayesian Estimation: A Flexible
Approach

	Functions for estimating models using a Hierarchical Bayesian (HB) framework. The flexibility comes in allowing the user to specify the likelihood function directly instead of assuming predetermined model structures. Types of models that can be estimated with this code include the family of discrete choice models (Multinomial Logit, Mixed Logit, Nested Logit, Error Components Logit and Latent Class) as well ordered response models like ordered probit and ordered logit. In addition, the package allows for flexibility in specifying parameters as either fixed (non-varying across individuals) or random with continuous distributions. Parameter distributions supported include normal, positive/negative log-normal, positive/negative censored normal, and the Johnson SB distribution. Kenneth Train's Matlab and Gauss code for doing Hierarchical Bayesian estimation has served as the basis for a few of the functions included in this package. These Matlab/Gauss functions have been rewritten to be optimized within R. Considerable code has been added to increase the flexibility and usability of the code base. Train's original Gauss and Matlab code can be found here: <http://elsa.berkeley.edu/Software/abstracts/train1006mxlhb.html> See Train's chapter on HB in Discrete Choice with Simulation here: <http://elsa.berkeley.edu/books/choice2.html>; and his paper on using HB with non-normal distributions here: <http://eml.berkeley.edu//~train/trainsonnier.pdf>. The authors would also like to thank the invaluable contributions of Stephane Hess and the Choice Modelling Centre: <https://cmc.leeds.ac.uk/>.
	"""
	
	homepage = "https://github.com/RSGInc/RSGHB"
	cran = "RSGHB" 

	version("1.2.2", md5="b160ce0504cfe501c2486035f1b06b4e")

	depends_on("r-mcmcpack", type=("build", "run"))
