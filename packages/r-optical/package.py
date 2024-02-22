# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptical(RPackage):
	"""Optimal Item Calibration

	The restricted optimal design method is implemented to optimally 
 allocate a set of items that require calibration to a group of examinees.
 The optimization process is based on the method described in detail by 
 Ul Hassan and Miller in their works published in (2019) 
 <doi:10.1177/0146621618824854> and (2021) <doi:10.1016/j.csda.2021.107177>.
 To use the method, preliminary item characteristics must be provided as input.
 These characteristics can either be expert guesses or based on previous
 calibration with a small number of examinees. The item characteristics
 should be described in the form of parameters for an Item Response
 Theory (IRT) model. These models can include the Rasch model, the
 2-parameter logistic model, the 3-parameter logistic model, or a mixture
 of these models. The output consists of a set of rules for each item
 that determine which examinees should be assigned to each item. The
 efficiency or gain achieved through the optimal design is quantified by
 comparing it to a random allocation. This comparison allows for an
 assessment of how much improvement or advantage is gained by using the
 optimal design approach. This work was supported by the Swedish Research Council
 (Vetenskapsrådet) Grant 2019-02706.
	"""
	
	homepage = "https://scenic555.github.io/optical/"
	cran = "optical" 

	version("1.7.1", md5="7f0310b8f58bf28ab0e42723127b79aa")

	depends_on("r@4.1:", type=("build", "run"))
