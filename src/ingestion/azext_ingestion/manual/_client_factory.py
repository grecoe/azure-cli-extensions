# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ITokenProvider import ITokenProvider
from azext_ingestion.manual.src.contracts.IPersistConfiguration import IPersistConfiguration

def cf_ingestion(cli_ctx, *_):
    """
    Default ingestion client currently unused.
    """

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    return None

def cf_token_get(cli_ctx, *_) -> ITokenProvider:
    """
    Client for acquiring a token. 
    """
    from .src._sp_token_provider import SPTokenConfigurationService
    return SPTokenConfigurationService()

def cf_platform_config(cli_ctx, *_) -> IPersistConfiguration:
    """
    Client for acquiring a token. 
    """
    from .src._osdu_persist_config import OSDUPersistConfiguration
    return OSDUPersistConfiguration()