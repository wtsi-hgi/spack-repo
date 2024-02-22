# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQlifetable(RPackage):
	"""Managing and Building of Quarterly Life Tables

	Manages, builds and computes statistics and datasets for the 
   construction of quarterly (sub-annual) life tables by exploiting micro-data from
   either a general or an insured population.
   References: 
   Pavía and Lledó (2022) <doi:10.1111/rssa.12769>.
   Pavía and Lledó (2023) <doi:10.1017/asb.2023.16>.
   Acknowledgements:
   The authors wish to thank Consellería de Educación, Universidades y Empleo, Generalitat Valenciana (grant AICO/2021/257), Ministerio de Economía e Innovación (grant PID2021-128228NB-I00) and Fundación Mapfre (grant 'Modelización espacial e intra-anual de la mortalidad en España. Una herramienta automática para el cálculo de productos de vida') for supporting this research.
	"""
	
	cran = "qlifetable" 

	version("0.0.2-4", md5="a8d3bb476d2d31e80b9f374253dfc929")

	depends_on("r@3.5:", type=("build", "run"))
