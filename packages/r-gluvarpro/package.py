# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGluvarpro(RPackage):
	"""Glucose Variability Measures from Continuous Glucose Monitoring
Data

	Calculate different glucose variability measures, 
 including average measures of glycemia, measures of glycemic variability and
 measures of glycemic risk, from continuous glucose monitoring data.
 Boris P. Kovatchev, Erik Otto, Daniel Cox, Linda Gonder-Frederick, and William Clarke (2006) <doi:10.2337/dc06-1085>.
 Jean-Pierre Le Floch, Philippe Escuyer, Eric Baudin, Dominique Baudon, and Leon Perlemuter (1990) <doi:10.2337/diacare.13.2.172>.
 C.M. McDonnell, S.M. Donath, S.I. Vidmar, G.A. Werther, and F.J. Cameron (2005) <doi:10.1089/dia.2005.7.253>.
 Everitt, Brian (1998) <doi:10.1111/j.1751-5823.2011.00149_2.x>.
 Becker, R. A., Chambers, J. M. and Wilks, A. R. (1988) <doi:10.2307/2234167>.
 Dougherty, R. L., Edelman, A. and Hyman, J. M. (1989) <doi:10.1090/S0025-5718-1989-0962209-1>.
 Tukey, J. W. (1977) <doi:10.1016/0377-2217(86)90209-2>.
 F. John Service (2013) <doi:10.2337/db12-1396>.
 Edmond A. Ryan, Tami Shandro, Kristy Green, Breay W. Paty, Peter A. Senior, David Bigam, A.M. James Shapiro, and Marie-Christine Vantyghem (2004) <doi:10.2337/diabetes.53.4.955>.
 F. John Service, George D. Molnar, John W. Rosevear, Eugene Ackerman, Leal C. Gatewood, William F. Taylor (1970) <doi:10.2337/diab.19.9.644>.
 Sarah E. Siegelaar, Frits Holleman, Joost B. L. Hoekstra, and J. Hans DeVries (2010) <doi:10.1210/er.2009-0021>.
 Gabor Marics, Zsofia Lendvai, Csaba Lodi, Levente Koncz, David Zakarias, Gyorgy Schuster, Borbala Mikos, Csaba Hermann, Attila J. Szabo, and Peter Toth-Heyn (2015) <doi:10.1186/s12938-015-0035-3>.
 Thomas Danne, Revital Nimri, Tadej Battelino, Richard M. Bergenstal, Kelly L. Close, J. Hans DeVries, SatishGarg, Lutz  Heinemann, Irl Hirsch, Stephanie A. Amiel, Roy Beck,  Emanuele Bosi, Bruce Buckingham, 
 ClaudioCobelli, Eyal Dassau, Francis J. Doyle, Simon Heller, Roman Hovorka, Weiping Jia, Tim Jones, Olga Kordonouri,Boris Kovatchev, Aaron Kowalski, Lori Laffel, David Maahs, Helen R. Murphy, Kirsten Nørgaard, 
 Christopher G.Parkin, Eric Renard, Banshi Saboo, Mauro Scharf, William V. Tamborlane, Stuart A. Weinzimer, and Moshe Phillip.International consensus on use of continuous glucose monitoring.Diabetes Care, 2017 <doi:10.2337/dc17-1600>.
	"""
	
	cran = "gluvarpro" 

	version("7.0", md5="7f123be3d53bc5249192833d24051d2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
