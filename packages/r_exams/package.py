# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExams(RPackage):
	"""Automatic Generation of Exams in R

	Automatic generation of exams based on exercises in Markdown or LaTeX format,
	possibly including R code for dynamic generation of exercise elements.
	Exercise types include single-choice and multiple-choice questions, arithmetic problems,
	string questions, and combinations thereof (cloze). Output formats include standalone
	files (PDF, HTML, Docx, ODT, ...), Moodle XML, QTI 1.2, QTI 2.1, Blackboard, Canvas, OpenOlat, ILIAS, TestVision,
	Particify, ARSnova, Kahoot!, Grasple, and TCExam. In addition to fully customizable PDF exams, a standardized PDF format
	(NOPS) is provided that can be printed, scanned, and automatically evaluated.
	"""
	
	homepage = "https://www.R-exams.org/"
	cran = "exams" 

	version("2.4-0", md5="976458e096b1036ac0bc4165ed4ba324")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
