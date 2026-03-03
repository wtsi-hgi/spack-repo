# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastexcel(PythonPackage):
    """A fast excel file reader for Python, written in Rust."""

    homepage = "https://github.com/ToucanToco/fastexcel"



    version("0.8.0-py312", sha256="fd005b6a762340b02332dfca2bd39516999009afa96e6aacbb2c78d4a29c22fc", expand=False, url="https://files.pythonhosted.org/packages/1d/f0/39d12f44d625ceaab09668245b032a8c56b182aec6aea59f1ada2ffd2157/fastexcel-0.8.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.8.0-py311", sha256="30f48104e5f88ec8d5f9a8d6110dce1b4064e6071ee877bd439e664bef9a0837", expand=False, url="https://files.pythonhosted.org/packages/86/40/19c7f198ed88f54a0b60c224885519cde0c818a52df841abaa752aa19d9f/fastexcel-0.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.8.0-py310", sha256="4e6b2e09221593de7562bdff132f9eb6df0872feb5a745f120e7ad899fcf8e88", expand=False, url="https://files.pythonhosted.org/packages/1c/27/e3b0e2ffb48161543ebca96cd66e72177656783770c06beaf2bb97b7aa61/fastexcel-0.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.8.0-py309", sha256="b8e2a27297b718c0e843445380cab4323bd94769709056f89aba03b45ffa5456", expand=False, url="https://files.pythonhosted.org/packages/30/00/217b3a83dc2b0d10aeee6b9f450339015070504d0d4419e1d3d1b1381274/fastexcel-0.8.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.8.0-py308", sha256="bc5305ab7134cc38bac5bb02acc86a99dfe30eae3f0bf8e89400df37717aa286", expand=False, url="https://files.pythonhosted.org/packages/82/87/d769bd641c957077fd2f6ab9b5da54c381527d1f7ac0f3ae72cfef25b0c5/fastexcel-0.8.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")

    depends_on("python@3.12", when="@0.8.0-py312")
    depends_on("python@3.11", when="@0.8.0-py311")
    depends_on("python@3.10", when="@0.8.0-py310")
    depends_on("python@3.9", when="@0.8.0-py309")
    depends_on("python@3.8", when="@0.8.0-py308")
