# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMallet(RPackage):
	"""An R Wrapper for the Java Mallet Topic Modeling Toolkit

	
  An R interface for the Java Machine Learning for Language Toolkit (mallet)
  <http://mallet.cs.umass.edu/> to estimate probabilistic topic models, such
  as Latent Dirichlet Allocation. We can use the R package to read textual 
  data into mallet from R objects, run the Java implementation of mallet 
  directly in R, and extract results as R objects. The Mallet toolkit 
  has many functions, this wrapper focuses on the topic modeling sub-package 
  written by David Mimno. The package uses the rJava package to connect to a 
  JVM.
	"""
	
	homepage = "https://github.com/mimno/RMallet"
	cran = "mallet" 

	version("1.3.0", md5="dad29fd305e82193bd90a4acc2bf08d7")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
