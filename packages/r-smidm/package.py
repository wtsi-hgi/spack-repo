# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmidm(RPackage):
	"""Statistical Modelling for Infectious Disease Management

	Statistical models for specific coronavirus disease 2019 use cases at German local health authorities. All models of Statistical modelling for infectious disease management 'smidm' are part of the decision support toolkit in the 'EsteR' project. More information is published in Sonja Jäckle, Rieke Alpers, Lisa Kühne, Jakob Schumacher, Benjamin Geisler, Max Westphal "'EsteR' – A Digital Toolkit for COVID-19 Decision Support in Local Health Authorities" (2022) <doi:10.3233/SHTI220799> and Sonja Jäckle, Elias Röger, Volker Dicken, Benjamin Geisler, Jakob Schumacher, Max Westphal "A Statistical Model to Assess Risk for Supporting COVID-19 Quarantine Decisions" (2021) <doi:10.3390/ijerph18179166>.
	"""
	
	homepage = "https://gitlab.cc-asp.fraunhofer.de/ester/smidm"
	cran = "smidm" 

	version("1.0", md5="46dafe337211ce2bd93c210133caae07")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
