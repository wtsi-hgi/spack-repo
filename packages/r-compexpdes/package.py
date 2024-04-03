# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompexpdes(RPackage):
	"""Computer Experiment Designs

	In computer experiments space-filling designs are having great impact. Most popularly used space-filling designs are Uniform designs (UDs), Latin hypercube designs (LHDs) etc. For further references one can see Mckay (1979) <DOI:10.1080/00401706.1979.10489755> and Fang (1980) <https://cir.nii.ac.jp/crid/1570291225616774784>. In this package, we have provided algorithms for generate efficient LHDs and UDs. Here, generated LHDs are efficient as they possess lower value of Maxpro measure, Phi_p value and Maximum Absolute Correlation (MAC) value. On the other hand, the produced UDs are having good space-filling property as they attained the lower bound of Discrete Discrepancy measure. 
	"""
	
	cran = "CompExpDes" 

	version("1.0.0", md5="a7e0784220a57ab900140f338de13149")

