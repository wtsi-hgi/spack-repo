# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJupyterHttpOverWs(PythonPackage):
    """Jupyter support for HTTP-over-ws"""

    homepage = "https://github.com/googlecolab/jupyter_http_over_ws"
    pypi = "jupyter-http-over-ws/jupyter_http_over_ws-0.0.8-py2.py3-none-any.whl"

    version(
        "0.0.1a1",
        sha256="4cc1956b878336c0670abbbad1ddef0975c18814707647a3b471b3fb683fb2d5",
        expand=False,
        url="https://files.pythonhosted.org/packages/56/9d/f3e02cb2b97b7baff908a3ee428df6ec978b793a2ae4d4be32f2f5bdb7e4/jupyter_http_over_ws-0.0.1a1-py2.py3-none-any.whl",
    )
    version(
        "0.0.1a2",
        sha256="08dbd49d040f21b493d624a356b1a7b583d9ee77ba8667ef10eda1f8c5aa9673",
        expand=False,
        url="https://files.pythonhosted.org/packages/db/20/0f171974abe1cce75e4709b6168107622c87bea5a5ac668900c768f82ea6/jupyter_http_over_ws-0.0.1a2-py2.py3-none-any.whl",
    )
    version(
        "0.0.1a3",
        sha256="a5ac3295af565d31faa2ac86ee58e86e17bacd893d78ec4d0cbd35a69afaa2c1",
        expand=False,
        url="https://files.pythonhosted.org/packages/22/2b/c9cd3b141afc87431bca9cb3823e2956b82e46a7b7088580abe408cdf3b5/jupyter_http_over_ws-0.0.1a3-py2.py3-none-any.whl",
    )
    version(
        "0.0.2",
        sha256="ea49831cf18fd626bdb436881f4d889e30987d5e673b910ef212de5a4f79d245",
        expand=False,
        url="https://files.pythonhosted.org/packages/55/e2/8d7f595d9f34d83a827ff0ede2ecb540a4b75b4309efb0510bffc064174e/jupyter_http_over_ws-0.0.2-py2.py3-none-any.whl",
    )
    version(
        "0.0.3",
        sha256="2c408e76015867c9e771b0e76220edacf6ba09f2b3629e2a9ee0145e2f014673",
        expand=False,
        url="https://files.pythonhosted.org/packages/a4/cb/a6ab5df2a43bb54181a49d2f407b4539b73761174909d6f39214bfaff9d6/jupyter_http_over_ws-0.0.3-py2.py3-none-any.whl",
    )
    version(
        "0.0.4",
        sha256="911d6e1ed9e8f79181c015de33f67fab59fb057152228841dcbc995265bdf1e7",
        expand=False,
        url="https://files.pythonhosted.org/packages/0b/8b/b1f76ed3d4cc39f1d7ef9e629a056b8b294acfeafab20efdea72aa0ec86e/jupyter_http_over_ws-0.0.4-py2.py3-none-any.whl",
    )
    version(
        "0.0.5",
        sha256="c69b26a731f94115d3a068ad08d893cd794723ecc1dca070a0558b424d0b32f5",
        expand=False,
        url="https://files.pythonhosted.org/packages/b0/2d/6d5a4ffde6acc0a99d6af5f2ca486bf60a78adb1cdbab066e2d8a96ccdb3/jupyter_http_over_ws-0.0.5-py2.py3-none-any.whl",
    )
    version(
        "0.0.6",
        sha256="e4b7829bd3a1dbdec98acfb872259e6c8ff3dba2e5172493376de67a11a1dd7f",
        expand=False,
        url="https://files.pythonhosted.org/packages/7f/e3/4f7044e988327a10bc459e3d3590c59c1cdbdb53c83670c8606d1fbee3c9/jupyter_http_over_ws-0.0.6-py2.py3-none-any.whl",
    )
    version(
        "0.0.7",
        sha256="75f2e01d6597e69247fe46f193fc3cc775f2894b718f60a8fafc4537f1ede746",
        expand=False,
        url="https://files.pythonhosted.org/packages/87/dd/356cacfa43aa87e2dbe7985a0cf8c9d964983d0914ff49853ac002e0639c/jupyter_http_over_ws-0.0.7-py2.py3-none-any.whl",
    )
    version(
        "0.0.8",
        sha256="3052a94929d9fb41e4fe33fc22c569e81e018b9454a923bd818599bf62ffd85a",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/b8/d0047d068facc913a354d14c4664b0ba99b8f30f8d66a1800e98549c06ce/jupyter_http_over_ws-0.0.8-py2.py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-notebook", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-tornado", type=("build", "run"))


# {'notebook(>=5.0)': ['0.0.1a1', '0.0.1a2', '0.0.1a3', '0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6', '0.0.7', '0.0.8'], 'six(>=1.4.0)': ['0.0.1a1', '0.0.1a2', '0.0.1a3', '0.0.2'], 'tornado(>=4.5)': ['0.0.1a1', '0.0.1a2', '0.0.1a3', '0.0.2', '0.0.3', '0.0.5', '0.0.6', '0.0.7', '0.0.8'], 'enum34(~=1.1)': ['0.0.2', '0.0.3', '0.0.4', '0.0.5', '0.0.6', '0.0.7'], 'six(>=1.6.0)': ['0.0.3', '0.0.4', '0.0.5', '0.0.6', '0.0.7', '0.0.8'], 'tornado(<6,>=4.5)': ['0.0.4'], 'enum34(~=1.1);python_version<"3.4"': ['0.0.8']}
