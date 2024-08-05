# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPyqtwebengineQt5(PythonPackage):
    """The subset of a Qt installation needed by PyQtWebEngine."""

    homepage = "https://www.riverbankcomputing.com/software/pyqt/"
    url = "https://files.pythonhosted.org/packages/3d/96/cb3db6e3730dd5684c9558d23ccd7153dd9747bdf0a25a0ecbb4880ac4cf/PyQtWebEngine_Qt5-5.15.14-py3-none-manylinux2014_x86_64.whl"

    version("5.15.14", sha256="2bc1fb0576802da609204d41df43787635216a310fadb6c81c89cf992bc63c52", expand=False)

