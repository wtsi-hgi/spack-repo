# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModernva(RPackage):
	"""An Implementation of Two Modern Education-Based Value-Added
Models

	Provides functions that fit two modern education-based value-added models.  
                 One of these models is the quantile value-added model.  This model 
                 permits estimating a school's value-added based on specific quantiles of 
                 the post-test distribution.  Estimating value-added based on quantiles 
                 of the post-test distribution provides a more complete picture of an 
                 education institution's contribution to learning for students of all 
                 abilities. See Page, G.L.; San Martín, E.; Orellana, J.; Gonzalez, J. (2017)
                 <doi:10.1111/rssa.12195> for more details.  The second model is a temporally 
                 dependent value-added model. This model takes into account the temporal 
                 dependence that may exist in school performance  between two cohorts in one 
                 of two ways.  The first is by modeling school  random effects with a 
                 non-stationary AR(1) process.  The second is by  modeling school effects 
                 based on previous cohort's post-test performance. In addition to more 
                 efficiently estimating value-added, this model permits making statements 
                 about the persistence of a schools effectiveness. The standard  value-added 
                 model is also an option.
	"""
	
	cran = "modernVA" 

	version("0.1.3", md5="a033f1d5acef1100d0999d432293408b")

