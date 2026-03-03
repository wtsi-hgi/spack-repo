# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGenomepy(PythonPackage):
    """Genes and genomes at your fingertips"""

    homepage = "https://github.com/vanheeringen-lab/genomepy"
    pypi = "genomepy/genomepy-0.9.3-py3-none-any.whl"

    version("0.0.1", sha256="9383ef4d2d7b7c008bf4150674c6058efa434235e4c08f2f1b201b888e424389")
    version("0.0.2", sha256="f3b31d979129c9314d36803c2311d33138a5a2e70286ca86341733c09b855697")
    version(
        "0.10.0",
        sha256="0abfd8ee358f8d8649420c61bdca3025559f59b41500ea35b5df18e3af167a5e",
        expand=False,
        url="https://files.pythonhosted.org/packages/ac/32/062a5c37ccb28d87712f9ecae80bc07e0f723ea36ff1b4c2107551217d86/genomepy-0.10.0-py3-none-any.whl",
    )
    version(
        "0.11.0",
        sha256="273cc60e707f3cfabfadb5a437a4c13fc9c79fe72dc1dfa7f8e7ef48662cd354",
        expand=False,
        url="https://files.pythonhosted.org/packages/9d/e9/3af303b74ecf29117e1cd9931d3bca17e73522b2121e5f3101d98d429a21/genomepy-0.11.0-py3-none-any.whl",
    )
    version(
        "0.11.1",
        sha256="98de59393b78c23e45ec803e3b0360cb9fb01d6e71194a7c50d17e9a3ab70978",
        expand=False,
        url="https://files.pythonhosted.org/packages/4a/d4/45216550f1016497ce997766ea5faa22b81754e5b567cfedd04b48871d74/genomepy-0.11.1-py3-none-any.whl",
    )
    version(
        "0.12.0",
        sha256="fb04083548b36ba7287cee158023d83b5d26bedbc9fa0e2d610f8cba192a5dd4",
        expand=False,
        url="https://files.pythonhosted.org/packages/e4/8b/3e5c7c57a159ed5b0e334422088cd54fbbf9db62c07f424b4f79e807aaf0/genomepy-0.12.0-py3-none-any.whl",
    )
    version(
        "0.13.0",
        sha256="43dd9cdfaa6d430b882a0fbdb617356e2ea7f4cea2d873d88113a5d26d9dbe8a",
        expand=False,
        url="https://files.pythonhosted.org/packages/77/87/49904695555c2ed68ce10385787b283fefea117d632199419f87213d58eb/genomepy-0.13.0-py3-none-any.whl",
    )
    version(
        "0.13.1",
        sha256="46d79e6e2696fb0df3eef4622a214a9131377e49086904cb2c34f42d822e209b",
        expand=False,
        url="https://files.pythonhosted.org/packages/8a/f4/ae358cc1ea19938eee2dca11dce66b3fb13898115349cf4c47a949d7bf21/genomepy-0.13.1-py3-none-any.whl",
    )
    version(
        "0.14.0",
        sha256="46bbd7d447e0d90be2da796bc049c121feecdf0a990d02f1ecec187ee1ff3f23",
        expand=False,
        url="https://files.pythonhosted.org/packages/0c/cb/c28dc8c13fade8ba04b83ab401d319920d47c94fbbd71a5c33a444436059/genomepy-0.14.0-py3-none-any.whl",
    )
    version(
        "0.15.0",
        sha256="a5344b30bee00d6238fd6ea8c9d51499cbcb474d32c325254330b297701870f3",
        expand=False,
        url="https://files.pythonhosted.org/packages/6e/69/2dfc9177d1f1b4dbeadb42dc7c48e5dc827f8d76640a65b186a5d9a85379/genomepy-0.15.0-py3-none-any.whl",
    )
    version(
        "0.16.0",
        sha256="995c77c3ff65fd6e81b3ccbeb7e1b1662d1c11be2ff31901ea48ab3f8dd28199",
        expand=False,
        url="https://files.pythonhosted.org/packages/01/48/ab173103bc43e6a4331f1a659eee28ef4541906decaf4dd60f9026e56db4/genomepy-0.16.0-py3-none-any.whl",
    )
    version(
        "0.16.1",
        sha256="820d46bce1503f66aa82e795a9a33e53a89e4d4f3f79b5c105ae452164f47635",
        expand=False,
        url="https://files.pythonhosted.org/packages/ae/35/6643405d6ff16684d5a25391c34ec9d09fc7169c19b081c4e3858d20b93f/genomepy-0.16.1-py3-none-any.whl",
    )
    version("0.2.1", sha256="2eac89557e658e6843350a56d14fbde23dfd44b1b5d7e20ba8b166fcbf2a3df7")
    version("0.2.2", sha256="cc66cd4ecae6db0fa339e3d806556a7a75515d1df640a226e633770bf1f64f34")
    version("0.2.3", sha256="3ed3405fc627a0f107c29c79e832e33517c0ea64a5a9f69a63eb8ceec1d2267d")
    version("0.3.0", sha256="bc381751e7cef7d2d825ed46135fcda8c7c0af81a9aa22af8efb6d7b498051a8")
    version("0.3.1", sha256="3ebdfca46504bedd1edfdb938d8c779a67fc7e1da0287c360c71b8b7434f2dd1")
    version("0.4.0", sha256="81cf2885b47812bfcf1194647f7f2cb3ee35c094c91b7c00db45ff3430592998")
    version("0.5.0", sha256="873143fe108f98c44c013c9137c594ccd8b6f09f43c62d8320932bfda824bce6")
    version("0.5.2", sha256="fa78b8d53b952ff200a6b7f7ed28aae64d57ef2a99bcb6df1bb4b16bef403895")
    version("0.5.4", sha256="713846f815dcb5cae73851c00b4bc9a8e97c44cb6616b3719ed9c0bccb47eea8")
    version("0.5.5", sha256="f6eabb8834d45aff9f22c17178c45f7445b518821d6185b10cb4d1479688e5db")
    version("0.6.0", sha256="13f171150868aceff5c1c0ae93f7bcc7420c9b81d914abd76fe3c0cb644d06d1")
    version("0.6.1", sha256="2caafeb2848cc129b68fa8a76bfed027a585ec9d3fd96b29f22b48caafc1b09c")
    version(
        "0.7.0",
        sha256="1b02b3c57708a661c8dfedc45c66c9893c85ba02810dc4ed35e1c9c7944410d6",
        expand=False,
        url="https://files.pythonhosted.org/packages/c9/98/131cbf35378ea162ccd4892edff7f23aebfe066afb4c7fafa104f5fdf502/genomepy-0.7.0-py3-none-any.whl",
    )
    version(
        "0.7.1",
        sha256="d2f6fcfb44ed745081f241aca74012f7fb6b4246d149f2c23717123590d4f02b",
        expand=False,
        url="https://files.pythonhosted.org/packages/03/e3/83e5bc3f5e78f9c4105fb1c0fd4c4170c5b864e3465e91940e3b607dc07e/genomepy-0.7.1-py3-none-any.whl",
    )
    version(
        "0.7.1a0",
        sha256="af67da9d0245a1a1927be8da6690980d036b01d25aca436a2ff19405ffed11b2",
        expand=False,
        url="https://files.pythonhosted.org/packages/9c/86/e40cc93d959cf37f5b64f5f2278d84d395993064c6bc9f962b18129129fc/genomepy-0.7.1a0-py3-none-any.whl",
    )
    version("0.7.2", sha256="f90e76da067c35206d5344e61de3068df4f22ae63683d1f7ad17da627af2c3d6")
    version("0.8.1", sha256="e4cec294c157a8e7cf36dba9edd3a3011e5be10ff98fac1b5d1aba72f89d2ec0")
    version("0.8.2", sha256="abc7ceceb9cc67f4c33e0287cf7dcd3a922d7961ce6fa0605aca684927a224e6")
    version("0.8.3", sha256="5c8fa4f418f7cf6904b54edc4cec3b5bce0d495dc79fdd13c73ec622dcdd76e7")
    version("0.8.4", sha256="c399cf97cb91e9324bcc9463fdb4eb4827dccc9cc16e3e3b44b5b9dc6e97e63e")
    version("0.9.0", sha256="b10539c3a8760c52144b80795a22f911d9dae056d09580f64b7ab5a42570f354")
    version("0.9.1", sha256="9f21490bde5157dfd054a0f8634b571a3eb9ef905cf679fdf2eefd2ce77e86aa")
    version(
        "0.9.2",
        sha256="346b81965862ed61855b21f0e77d708ddbdbc20a808ebb48936c4a2afb9ccb85",
        expand=False,
        url="https://files.pythonhosted.org/packages/f8/1e/1588671c1a94f62dbdfad912e63cd2ab3c46e462d9c40af76b9c7da1fde0/genomepy-0.9.2-py3-none-any.whl",
    )
    version(
        "0.9.3",
        sha256="574d9c8e7831275f53dff0adaaf4e1edfe16f04baced4c324dc266dfff858e84",
        expand=False,
        url="https://files.pythonhosted.org/packages/c9/28/6c2cbf8ea69f2c7a90a19f293653dbd786f47c085cfecc181ea7b51a7444/genomepy-0.9.3-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    with default_args(type=("build", "run")):
        depends_on("python@3.7:")
        depends_on("py-appdirs")
        depends_on("py-biopython")
        depends_on("py-numpy")
        depends_on("py-pandas")
        depends_on("py-bucketcache")
        depends_on("py-click")
        depends_on("py-colorama")
        depends_on("py-norns")
        depends_on("py-pyfaidx")
        depends_on("py-requests")
        depends_on("py-tqdm")
        depends_on("py-loguru")
        depends_on("py-mygene")
        depends_on("py-diskcache@5.3:")
        depends_on("py-psutil")
        depends_on("py-xmltodict")
        depends_on("py-filelock")
        depends_on("py-joblib")
        depends_on("py-mysql-connector-python")


# {'appdirs': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'biopython(>=1.73)': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'bucketcache': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'click': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'colorama': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1', '0.9.2', '0.9.3'], 'joblib': ['0.10.0', '0.11.0', '0.11.1', '0.12.0'], 'loguru': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'mygene': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'mysql-connector-python': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'norns(>=0.1.5)': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'numpy': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'pandas': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'pyfaidx(>=0.5.7)': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.9.2', '0.9.3'], 'requests': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1', '0.7.0', '0.7.1', '0.7.1a0', '0.9.2', '0.9.3'], 'tqdm(>=4.51)': ['0.10.0', '0.11.0', '0.11.1', '0.12.0', '0.13.0', '0.13.1', '0.9.2', '0.9.3'], 'diskcache': ['0.13.0', '0.13.1', '0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'biopython>=1.73': ['0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'filelock': ['0.14.0'], 'norns>=0.1.5': ['0.14.0'], 'pyfaidx>=0.5.7': ['0.14.0'], 'tqdm>=4.51': ['0.14.0', '0.15.0', '0.16.0', '0.16.1'], 'filelock>=3.5': ['0.15.0', '0.16.0', '0.16.1'], 'norns>=0.1.6': ['0.15.0', '0.16.0', '0.16.1'], 'pyfaidx>=0.7.2.1': ['0.15.0', '0.16.0', '0.16.1'], 'pyfaidx(>=0.5.1)': ['0.7.0', '0.7.1', '0.7.1a0'], 'xmltodict': ['0.7.0', '0.7.1', '0.7.1a0'], 'psutil': ['0.7.0', '0.7.1', '0.7.1a0']}
