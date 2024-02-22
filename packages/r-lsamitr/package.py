# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsamitr(RPackage):
	"""Daten, Beispiele und Funktionen zu 'Large-Scale Assessment mit
R'

	Dieses R-Paket stellt Zusatzmaterial in Form von Daten, Funktionen
             und R-Hilfe-Seiten für den Herausgeberband Breit, S. und Schreiner, 
             C. (Hrsg.). (2016). "Large-Scale Assessment mit R: Methodische Grundlagen 
             der österreichischen Bildungsstandardüberprüfung." Wien: facultas. 
             (ISBN: 978-3-7089-1343-8, <https://www.iqs.gv.at/themen/bildungsforschung/publikationen/veroeffentlichte-publikationen>) zur 
             Verfügung.
	"""
	
	homepage = "https://www.iqs.gv.at/themen/bildungsforschung/publikationen/veroeffentlichte-publikationen"
	cran = "LSAmitR" 

	version("1.0-3", md5="4f160c94e59032bd08ffac529c91f9f3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
