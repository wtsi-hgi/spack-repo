# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH0(RPackage):
	"""A Robust Bayesian Meta-Analysis for Estimating the Hubble
Constant via Time Delay Cosmography

	We provide a toolbox to conduct a Bayesian meta-analysis for estimating the current expansion rate of the Universe, called the Hubble constant H0, via time delay cosmography. The input data are Fermat potential difference and time delay estimates. For a robust inference, we assume a Student's t error for these inputs. Given these inputs, the meta-analysis produces posterior samples of the model parameters including the Hubble constant via Metropolis-Hastings within Gibbs. The package provides an option to implement repelling-attracting Metropolis-Hastings within Gibbs in a case where the parameter space has multiple modes.
	"""
	
	cran = "h0" 

	version("1.0.1", md5="d0d7ec65e08bf919e131e6ec6b50633a", url="https://cran.r-project.org/src/contrib/h0_1.0.1.tar.gz")

	depends_on("r@2.2:", type=("build", "run"))
