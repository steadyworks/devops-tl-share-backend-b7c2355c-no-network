from uuid import UUID

from fastapi import Request
from pydantic import BaseModel

from backend.lib.request.context import RequestContext
from backend.route_handler.base import RouteHandler, enforce_response_model


class SharePhotobookRequest(BaseModel):
    raw_emails_to_share: str
    invited_user_ids: list[UUID] = []
    custom_message: str = ""
    role: str = "viewer"  # Default role can be 'viewer', 'editor


class SharePhotobookResponse(BaseModel):
    success: bool
    message: str
    photobook_id: UUID
    user_id: UUID


class SharePhotobookAutocompleteResponse(BaseModel):
    emails: list[str]
    user_ids: list[UUID]


class ShareAPIHandler(RouteHandler):
    def register_routes(self) -> None:
        self.route(
            "/api/share/photobooks/{photobook_id}",
            "share_photobook",
            methods=["POST"],
        )
        self.route(
            "/api/share/get_share_autocomplete_options",
            "get_share_autocomplete_options",
            methods=["GET"],
        )

    @enforce_response_model
    async def get_share_autocomplete_options(
        self,
        request: Request,
    ):
        pass

    @enforce_response_model
    async def share_photobook(
        self,
        request: Request,
        photobook_id: UUID,
    ) -> SharePhotobookResponse:
        request_context: RequestContext = await self.get_request_context(
            request
        )

        # Here you would implement the logic to share the photobook
        # For example, create a share entry in the database
        pass
