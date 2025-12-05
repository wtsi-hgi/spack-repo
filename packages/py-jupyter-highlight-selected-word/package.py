# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJupyterHighlightSelectedWord(PythonPackage):
    """Highlight each occurrence of the selected word inside classic Jupyter notebooks."""

    homepage = "https://github.com/jcb91/jupyter_highlight_selected_word"
    pypi = "jupyter_highlight_selected_word/jupyter_highlight_selected_word-0.2.0.tar.gz"

    version("0.2.0", sha256="9fa740424859a807950ca08d2bfd28a35154cd32dd6d50ac4e0950022adc0e7b")

    depends_on("py-setuptools", type="build")
    depends_on("py-notebook", type="run")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import jupyter_highlight_selected_word")
